package main

import "fmt"

type UndergroundSystem struct {
	distanceStats map[string]map[string]int
	tempStations  map[int]string
	tempTime      map[int]int
}

func UndergroundSystemConstructor() UndergroundSystem {
	return UndergroundSystem{
		distanceStats: make(map[string]map[string]int),
		tempStations:  make(map[int]string),
		tempTime:      make(map[int]int),
	}
}

func (this *UndergroundSystem) CheckIn(id int, stationName string, t int) {
	this.tempStations[id] = stationName
	this.tempTime[id] = t
}

func (this *UndergroundSystem) CheckOut(id int, stationName string, t int) {
	prevStationName := this.tempStations[id]
	startTime := this.tempTime[id]
	delete(this.tempStations, id)
	delete(this.tempTime, id)

	srcDes := prevStationName + "-" + stationName
	if this.distanceStats[srcDes] == nil {
		this.distanceStats[srcDes] = make(map[string]int)
	}
	this.distanceStats[srcDes]["count"]++
	this.distanceStats[srcDes]["sum"] += t - startTime
}

func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
	srcDes := startStation + "-" + endStation
	return float64(this.distanceStats[srcDes]["sum"]) / float64(this.distanceStats[srcDes]["count"])
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * param_3 := obj.GetAverageTime(startStation,endStation);
 */

func main() {
	obj := UndergroundSystemConstructor()
	obj.CheckIn(45, "Leyton", 3)
	obj.CheckIn(32, "Paradise", 8)
	obj.CheckIn(27, "Leyton", 10)
	obj.CheckOut(45, "Waterloo", 15)
	obj.CheckOut(27, "Waterloo", 20)
	obj.CheckOut(32, "Cambridge", 22)
	fmt.Println(obj.GetAverageTime("Paradise", "Cambridge"))
	fmt.Println(obj.GetAverageTime("Leyton", "Waterloo"))
	obj.CheckIn(10, "Leyton", 24)
	fmt.Println(obj.GetAverageTime("Leyton", "Waterloo"))
	obj.CheckOut(10, "Waterloo", 38)
	fmt.Println(obj.GetAverageTime("Leyton", "Waterloo"))
}
