set terminal postscript eps enhanced "Times New Roman" 20
set output "entrada2.eps"
set notitle
set encoding utf8

set ylabel "Tempo de execução (s)"
set xlabel "Porcentagem do treino"


set grid

set yrange [0:0.8]
set xtics 10

#set key outside right top
set key right bot
set key box linestyle 1

plot  \
  "entrada.dat" using 1:3  with linespoints title 'jaccard k=7' lc rgb 'blue' lw 4
