package main

import "fmt"

type ParkingSystem struct {
	bigCount    int
	mediumCount int
	smallCount  int
}

func ParkingSystemConstructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{bigCount: big, mediumCount: medium, smallCount: small}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	switch carType {
	case 1:
		if this.bigCount == 0 {
			return false
		}
		this.bigCount--
	case 2:
		if this.mediumCount == 0 {
			return false
		}
		this.mediumCount--
	case 3:
		if this.smallCount == 0 {
			return false
		}
		this.smallCount--
	}
	return true
}

func main() {
	obj := ParkingSystemConstructor(1, 1, 0)
	fmt.Println(obj.AddCar(1))
	fmt.Println(obj.AddCar(2))
	fmt.Println(obj.AddCar(3))
	fmt.Println(obj.AddCar(1))
}
