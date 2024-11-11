package main

import (
	"fmt"
)

func main() {
	fmt.Println("你好 golang")
	fmt.Print("你好")
	fmt.Printf("你好")
	fmt.Print("A", "B", "C")
	fmt.Printf("A", "B", "C")
	fmt.Println("A", "B", "C")
	// -------------------------
	// var a int = 10
	// var b int = 3
	// var c int = 5
	// fmt.Println("a=", a, "b=", b, "c=", c)
	// fmt.Printf("a=%v b=%v c=%v", a, b, c)
	a := 10
	b := 20
	c := 30
	fmt.Println("a=", a, "b=", b, "c=", c)
}
