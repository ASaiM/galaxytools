library('getopt')

option_specification = matrix(c(
  'input_file', 'i', 2, 'character',
  'names', 'a', 2, 'character',
  'replace_null','u',2,'logical',
  'order','w',2,'logical',
  'header','y',2,'logical'
), byrow=TRUE, ncol=4);

options = getopt(option_specification);

header = TRUE
if(!is.null(options$header)) header = options$header

data = read.table(options$input_file, sep = '\t', h = header)
if(!is.null(options$replace_null) && options$replace_null){
  data[data == 0] = NA
}
if(!is.null(options$order) && options$order){
  order = order(data[,2])
  data = data[order,]
} 

names = c('file1')

if(!is.null(options$names)) names = unlist(strsplit(options$names))
plot_barplot <- function(){
    par(las=2)
    par(mar=margin)
    barplot(t(data[, data_columns]), horiz = T, xlab = xlab, beside=TRUE,
        names.arg = data[, names_column], col = col, cex.names=0.7, 
        cex.axis = 0.8, log = log)
    legend(legend_pos, legend = names, fill = col, cex = 0.7)
}

