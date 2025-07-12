(defpackage :lillys-lasagna
  (:use :cl)
  (:export :expected-time-in-oven
           :remaining-minutes-in-oven
           :preparation-time-in-minutes
           :elapsed-time-in-minutes))

(in-package :lillys-lasagna)

(defun expected-time-in-oven () "The expected time the lasagna is in the oven" (+ 0 337))

(defun remaining-minutes-in-oven (oven-time) "The remaining time the lasagna is in the oven" (- 337 oven-time))

(defun preparation-time-in-minutes (layers) "The number of minutes it takes to prepare the layers" (* 19 layers))

(defun elapsed-time-in-minutes (layers oven-time) "arglegargle" (+ (preparation-time-in-minutes layers) oven-time))