set terminal postscript eps enhanced "Times New Roman" 20
set output "entrada.eps"
set notitle
set encoding utf8

set ylabel "Acurácia (%)"
set xlabel "Porcentagem do treino"

set grid

set yrange [0:0.8]
set xtics 10

#set key outside right top
set key right bot
set key box linestyle 1

plot  \
  "entrada.dat" using 1:2  with linespoints title 'jaccard k=7' lt 1 lc rgb 'blue' lw 4 , \
  "entrada2.dat" using 1:2  with linespoints title 'euclidean k=30' lt 1 lc rgb 'red' lw 4
