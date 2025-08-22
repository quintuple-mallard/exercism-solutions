package collatzconjecture

import "errors"
func CollatzConjecture(n int) (int, error) {
    if n < 1 {
        return 0, errors.New("number must be positive")
    }
	if n == 1 {
        return 0, nil
    } else if n % 2 == 0 {
      nextStep, _ := CollatzConjecture(n / 2)
      return 1 + nextStep, nil
    }
    nextStep, _ := CollatzConjecture(n * 3 + 1)
    return 1 + nextStep, nil
}
