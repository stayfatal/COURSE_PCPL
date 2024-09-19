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
			log.Println("incorrect input")
			r.Reset(os.Stdin)
			continue
		}

		return a, b, c
	}
}

func calculateAndPrintEquation(a, b, c int) {
	d := b*b - 4*a*c

	switch {
	case d > 0:
		t1 := (-float64(b) - math.Sqrt(float64(d))) / (2.0 * float64(a))
		t2 := (-float64(b) + math.Sqrt(float64(d))) / (2.0 * float64(a))

		var roots []float64
		if t1 >= 0 {
			roots = append(roots, math.Sqrt(t1), -math.Sqrt(t1))
		}
		if t2 >= 0 {
			roots = append(roots, math.Sqrt(t2), -math.Sqrt(t2))
		}

		if len(roots) > 0 {
			fmt.Println("Roots:", roots)
		} else {
			fmt.Println("No real roots")
		}

	case d == 0:
		t := -float64(b) / (2.0 * float64(a))
		if t >= 0 {
			fmt.Println("Roots:", math.Sqrt(t), -math.Sqrt(t))
		} else {
			fmt.Println("No real roots")
		}

	case d < 0:
		fmt.Println("Discriminant < 0, no real roots")
	}
}
