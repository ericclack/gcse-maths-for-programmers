#lang racket

(require math/number-theory)

(define (e-seq n)
  ;; Sum of sequence 1 / i! for i = 0 ... n
  (cond
    [(= n 0) 1]
    [else (+ (/ 1
                (factorial n))
             (e-seq (sub1 n)))]))


(define (h-seq n)
  ;; Sum of sequence 1 / 2^i for i = 0 ... n
  (cond
    [(= n 1) 1/2]
    [else (+ (/ 1
                (expt 2 n))
             (h-seq (sub1 n)))]))
