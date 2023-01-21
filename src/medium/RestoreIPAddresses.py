class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        return self.generate_ip_addresses(s, 3)

    def generate_ip_addresses(self, s: str, remaining_dots: int) -> list:
        # print('generate_ip_addresses', s, remaining_dots)

        last_string = s.split('.')[-1]

        if remaining_dots == 0:
            if self.is_valid_ip_part(last_string):
                return [s]
            return []

        results = []

        for i in range(1, len(last_string)):
            candidate_string = last_string[0:i]
            # print(candidate_string)

            if int(candidate_string) > 255:
                # print('two')
                break

            if self.is_valid_ip_part(candidate_string):
                # print('three')
                new_string = '.'.join(s.split('.')[0:-1] + [candidate_string, last_string[i:]])
                # print(new_string)
                results += self.generate_ip_addresses(new_string, remaining_dots - 1)

        return results

    def is_valid_ip_part(self, ip_part: str) -> bool:
        if len(ip_part) < 1:
            return False

        # print('ip_part', ip_part)

        if len(ip_part) > 1 and ip_part[0] == '0':
            # print('44')
            return False

        if int(ip_part) < 0:
            # print('22')
            return False

        if int(ip_part) > 255:
            # print('33')
            return False

        return True
