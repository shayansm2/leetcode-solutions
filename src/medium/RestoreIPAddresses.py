class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        return self.generate_ip_addresses(s, 3)

    def generate_ip_addresses(self, s: str, remaining_dots: int) -> list:
        last_string = s.split('.')[-1]

        if remaining_dots == 0:
            if self.is_valid_ip_part(last_string):
                return [s]
            return []

        results = []

        for i in range(1, len(last_string)):
            candidate_string = last_string[0:i]

            if int(candidate_string) > 255:
                break

            if self.is_valid_ip_part(candidate_string):
                new_string = '.'.join(s.split('.')[0:-1] + [candidate_string, last_string[i:]])
                results += self.generate_ip_addresses(new_string, remaining_dots - 1)

        return results

    def is_valid_ip_part(self, ip_part: str) -> bool:
        if len(ip_part) < 1:
            return False

        if len(ip_part) > 1 and ip_part[0] == '0':
            return False

        if int(ip_part) < 0:
            return False

        if int(ip_part) > 255:
            return False

        return True
