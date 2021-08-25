
/* Είπαμε ότι το κομμάτι του κώδικα που παίρνει σαν είσοδο 
κάποιο πρόγραμμα/κώδικα και βγάζει σαν έξοδο ένα string με το όνομα
της γλώσσας είναι έτοιμο */


require('shelljs/global');

if (x = "Python") {var x1=exec('autopep8 --in-place --aggressive --aggressive <filename>').stdout; };

else if (x= "Javascript") {var x2=exec('npx eslint .').stdout; };

else if (x= "Java") {var x3= exec('walkmod apply').stdout;};

else if x= "Typescript") {var x3=exec('npx eslint . --ext .js,.jsx,.ts,.tsx)').stdout;};



/* pull request*/
