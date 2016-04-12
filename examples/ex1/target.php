#!/usr/bin/env php

<?php

$a = 4;
print "$a\n";

print 1 . "\n";
print "hello world\n";
print 1 .' '. 2 .' '. 'three' .' '. "$a\n";

$b = ['A','B','C'];
$b[1] = 'X';
$b[] = 'D';
print_r($b);

?>
