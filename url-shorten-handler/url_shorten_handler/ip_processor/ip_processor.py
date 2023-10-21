from collections import Counter, defaultdict

import httpx
from httpx import Response

from url_shorten_handler.util import logging


class IPAddressProcessor:
    API_URL = "http://ip-api.com/batch"
    FIELDS = "country,query"
    EMPTY_DICT = {}

    def process_ip_addresses(self, addresses: list) -> dict:
        address_map = Counter(addresses)
        chunks = self._create_chunks(address_map)
        address_responses = self._fetch_address_data(chunks)
        return self._aggregate_country_clicks(address_responses, address_map)

    def _fetch_address_data(self, chunks: list) -> list:
        responses = []

        for chunk in chunks:
            formatted_ips = [{"query": ip, "fields": self.FIELDS} for ip in chunk]
            response_data: Response = self._send_request(formatted_ips)
            if not response_data:
                break
            responses.append(response_data)

        return responses

    def _send_request(self, formatted_ips: list) -> Response | None:
        response = httpx.post(self.API_URL, json=formatted_ips)

        if response.status_code == 429:
            logging.warn(f"Calls to {self.API_URL} have been rate limited.")
            return None  # Return None or an empty list if you get a 429
        response.raise_for_status()

        return response.json()

    def _aggregate_country_clicks(self, address_responses: list, address_map: Counter) -> dict:
        if not address_responses:
            return self.EMPTY_DICT

        country_clicks = defaultdict(int)
        for address in address_responses[0]:
            country_clicks[address["country"]] = address_map[address["query"]]

        return dict(country_clicks)

    @staticmethod
    def _create_chunks(address_map: Counter) -> list:
        return [list(address_map.keys())[i : i + 100] for i in range(0, len(address_map), 100)]

    @staticmethod
    def aggregate_dicts(dict_one: dict, dict_two: dict) -> dict:
        return {
            key: dict_one.get(key, 0) + dict_two.get(key, 0)
            for key in set(dict_one) | set(dict_two)
        }