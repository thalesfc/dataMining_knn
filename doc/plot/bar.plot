set terminal postscript eps enhanced "Times New Roman" 20
set output "distance.eps"
set notitle
set encoding utf8

set ylabel "Acurácia (%)"
set xlabel "Número de vizinhos (k)"


set grid

set yrange [0:0.8]
set xtics 10

set style fill solid

set key box linestyle 1

plot "distance.dat" using 2: xtic(1) with histogram notitle
