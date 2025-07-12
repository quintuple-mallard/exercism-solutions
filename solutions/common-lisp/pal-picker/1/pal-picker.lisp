(defpackage :pal-picker
  (:use :cl)
  (:export :pal-picker :habitat-fitter :feeding-time-p
           :pet :play-fetch))

(in-package :pal-picker)

(defun pal-picker (personality)(case personality
                                 (:lazy "Cat")
                                 (:energetic "Dog")
                                 (:quiet "Fish")
                                 (:hungry "Rabbit")
                                 (:talkative "Bird")
                                 (otherwise "I don't know... A dragon?")
))

(defun habitat-fitter (weight)(cond
  ((<= 40 weight) :massive)
  ((<= 20 weight) :large)
  ((<= 10 weight) :medium)
  ((< 0 weight) :small)
  (t :just-your-imagination)                              
  ))

(defun feeding-time-p (fullness) (if (< 20 fullness) "All is well." "It's feeding time!")
  )

(defun pet (pet) (when (string= pet "Fish") "Maybe not with this pet..."))

(defun play-fetch (pet) (unless (string= pet "Dog") "Maybe not with this pet..."))
