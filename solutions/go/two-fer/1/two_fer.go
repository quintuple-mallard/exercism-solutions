// Exercism exercise Two Fer.
package twofer

import "fmt"

// returns One for me, one for {you|name}.
func ShareWith(name string) string {
    
    if name == "" {
        name = "you"
    }
	return fmt.Sprintf("One for %s, one for me.", name)
}
