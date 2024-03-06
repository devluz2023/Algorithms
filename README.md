coudl you generate a typescript code

input 
1 - home/fabio/julio/file1.txt
2 - home/fabio/julio/file2.txt
3 - home/fabio/file3.txt
4 - home/fabio/file4.txt
5 - home/file5.txt
6 - faluz/file6.txt
7 - luz/file8.csv
8 - luz/file9.txt
9 - luz/file10.csv

output
interface node{
    parent:string;
    children:string;
}
 [
{parent = /     ,  children = home },
{parent =home   ,  children = fabio},
{parent =fabio  ,  children = julio},
{parent =julio  ,  children = file1.txt},
{parent =julio  ,  children = file2.txt},
{parent =fabio  ,  children = file3.txt},
{parent =fabio  ,  children = file4.txt},
{parent =home   ,  children = file5.txt} ,
{parent =/      ,  children = faluz},
{parent =faluz  ,  children = file6.txt},
{parent =/      ,  children = luz},
{parent =luz    ,  children = file8.csv},
{parent =luz    ,  children = file9.txt},
{parent =luz    ,  children = file10.csv}
]

your-output
[
  { parent: undefined, children: 'home' },
  { parent: 'home', children: 'fabio' },
  { parent: 'fabio', children: 'julio' },
  { parent: 'julio', children: 'file1.txt' },
  { parent: 'julio', children: 'file2.txt' },
  { parent: 'fabio', children: 'file3.txt' },
  { parent: 'fabio', children: 'file4.txt' },
  { parent: 'home', children: 'file5.txt' },
  { parent: undefined, children: 'faluz' },
  { parent: 'faluz', children: 'file6.txt' },
  { parent: undefined, children: 'luz' },
  { parent: 'luz', children: 'file8.csv' },
  { parent: 'luz', children: 'file9.txt' },
  { parent: 'luz', children: 'file10.csv' }
]


todo ser humano ama?
ou ama Deus
ou ama o Espirito
ou ama a mae
ou ama o pai
ou ama o irmao
ou ama o amigo
ou ama o colega
ou ama o conhecido
ou amaa algum animal
ou ama alguma flor
ou ama algum objeto
ou ama algum pergonagem cientifico?
isso esta corrto, todo ser humano ama?

o amor reflete em novos valores , em nossas 
crencas , na forma como vemos a realidade e em nosso comportamento?

dentro os itens listados para vivermos um nacao justa igualitaria e democratica
como os valores individuais citados sao importantes para alcarmos esses objetivos?

paises com maiores indices de felicidade e idh tende serem perssoas mais amorosas?
no caso da resposta for sim. qual dos valores acima esses cidadados mais valorizam?

o amor causa dependencia emocial? o amor e como um vicio? que quando amamos demais uma cosia
pode nos causar irritacao e frustacao essa ausencia de amor, no que chariamos de carencia emocial ou ciumes?

jesus e paulo falaram muito sobre o amor?
qual a importncia do amor para saude nossa saude menatal?

como o amor pode nos libertar de magoas, racncor e ressentimentos?


