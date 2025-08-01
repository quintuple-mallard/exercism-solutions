(defpackage :pizza-pi
  (:use :cl)
  (:export :dough-calculator :pizzas-per-cube
           :size-from-sauce :fair-share-p))

(in-package :pizza-pi)

(defun dough-calculator (pizzas diameter)
  (round (* pizzas (+ (/ (* pi diameter 45) 20) 200)))
  )

(defun size-from-sauce (sauce)
  (sqrt (/ (* 40 sauce) (* 3 pi)))
  )

(defun pizzas-per-cube (l d)
  ( floor ( / ( * 2 ( expt l 3 )) (* 3 pi (expt d 2))))
  )
(defun fair-share-p (pizzas friends)
  (= 0 (mod (* 8 pizzas) friends))
  )
