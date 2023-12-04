package main

func largestGoodInteger(num string) string {
	var result string
	for i := 0; i < len(num)-2; i++ {
		if num[i] == num[i+1] && num[i+1] == num[i+2] {
			if result < num[i:i+3] {
				result = num[i : i+3]
			}
		}
	}
	return result
}
