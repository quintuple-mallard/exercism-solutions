(defpackage :raindrops
  (:use :cl)
  (:export :convert))

(in-package :raindrops)
(defun convert (number)
  (let ((sound-output "")) ; Initialize an empty string to build the output
    
    (when (= 0 (mod number 3)) 
      (setf sound-output (concatenate 'string sound-output "Pling")))

    (when (= 0 (mod number 5))
      (setf sound-output (concatenate 'string sound-output "Plang")))
    
    (when (= 0 (mod number 7))
      (setf sound-output (concatenate 'string sound-output "Plong")))
    
    
    (if (string= sound-output "")
        (princ-to-string number) 
        sound-output)))          
