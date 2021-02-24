package cmd

// Stack represent program stack
type Stack []interface{}

func (s *Stack) push(i interface{}) {
	*s = append(*s, i)
}

func (s *Stack) pop() interface{} {
	if len(*s) == 0 {
		panic("stack is empty unable to pop")
	}

	result := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]

	return result
}
