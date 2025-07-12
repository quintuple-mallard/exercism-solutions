(defpackage :leap
  (:use :cl)
  (:export :leap-year-p))

(in-package :leap)

(defun leap-year-p (year)
  (or (and
   (= 0 (mod year 4))
   (not (= 0 (mod year 100)))) (= 0 (mod year 400))))
