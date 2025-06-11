package main

func predictPartyVictory(senate string) string {
	queue := ""
	for len(senate) > 0 {
		char := string(senate[0])
		senate = senate[1:]
		if len(queue) == 0 || string(queue[0]) == char {
			queue += char
		} else {
			senate += string(queue[0])
			queue = queue[1:]
		}
	}
	if string(queue[0]) == "R" {
		return "Radiant"
	}
	return "Dire"
}

// DR RDRDRDRD DRDRDR
// D_R_R_R_R_D_D_D_
// D___R_R_R_______
// ______R_R_______
