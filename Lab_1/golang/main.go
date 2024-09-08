package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

func main() {
	args := os.Args
	var a, b, c int
	if len(args) == 4 {
		a, b, c = readFromArgs(args)
	} else {
		a, b, c = readFromConsole()
	}

	calculateAndPrintEquation(a, b, c)
}

func readFromArgs(args []string) (a, b, c int) {
	a, err := strconv.Atoi(args[1])
	if err != nil {
		log.Fatal("incorrect arguments in command line")
	}

	b, err = strconv.Atoi(args[2])
	if err != nil {
		log.Fatal("incorrect arguments in command line")
	}

	c, err = strconv.Atoi(args[3])
	if err != nil {
		log.Fatal("incorrect arguments in command line")
	}

	return
}

func readFromConsole() (int, int, int) {
	var a, b, c int
	r := bufio.NewReader(os.Stdin)
	for {
		_, err := fmt.Fscanf(r, "%d %d %d\n", &a, &b, &c)
		if err != nil {
			log.Println(err)
			r.Reset(os.Stdin)
			continue
		}

		return a, b, c
	}
}

func calculateAndPrintEquation(a, b, c int) {
	d := int(math.Pow(float64(b), 2)) - 4*a*c
	switch {
	case d > 0:
		fmt.Printf("Ans 1: %f\n", (-float64(b)-math.Sqrt(float64(d)))/(2.0*float64(a)))
		fmt.Printf("Ans 2: %f\n", (-float64(b)+math.Sqrt(float64(d)))/(2.0*float64(a)))
	case d < 0:
		fmt.Println("discriminant < 0")
	case d == 0:
		fmt.Printf("Ans 1: %f\n", -float64(b)/(2.0*float64(a)))
	}
}
