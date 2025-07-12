(defpackage :resistor-color
  (:use :cl)
  (:export :color-code
           :colors))

(in-package :resistor-color)

(defun color-code (color) (cond                       
    ((string= color "black") 0)
    ((string= color "brown") 1)
    ((string= color "red") 2)
    ((string= color "orange") 3)
    ((string= color "yellow") 4)
    ((string= color "green") 5)
    ((string= color "blue") 6)
    ((string= color "violet") 7)
    ((string= color "grey") 8)
    ((string= color "white") 9)
                            ))

(defun colors () (list "black" "brown" "red" "orange" "yellow" "green" "blue" "violet" "grey" "white"))
