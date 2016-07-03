#!/usr/bin/perl
use strict;
use warnings;

sub trim { my $s = shift; $s =~ s/^\s+|\s+$//g; return $s };
sub printdata { my $s = shift; print "Name: $s->[0], Phone no.: $s->[1]\nMarks: $s->[2], $s->[3], $s->[4]\n"; }

my $help = "manage-students.pl: student data management script\n" .
           "    usage: ./manage-students.pl <datafile> [<command>] [<command-opts>]\n" .
           "\n" .
           "commands:\n" .
           "    show [<index>] : display data of student at <index>, or all students if no index specified\n" .
           "    add            : add a student to the data file\n" .
           "    edit <index>   : edit the data of student at index\n"; 

my $file = $ARGV[0] or die "You need to provide a filename in command argument\n\n$help";
open(my $students, '<', $file) or die "Could not open '$file'\n";

my $command = $ARGV[1] // "show";
my $index = $ARGV[2] // "all";

my @data;

while (my $line = <$students>) {
    $line = trim("$line");
    my @linedata = split ',', $line;
    foreach my $i (0..4) {
        $linedata[$i] = trim("$linedata[$i]");
        $data[$. - 1][$i] = $linedata[$i];
    }
}

close $students;

if ($command eq "show") {
    if ($index eq "all") {
        foreach my $s (@data) {
            printdata($s);
        }
    } else {
        printdata($data[$index]);
    }
} elsif ($command eq "add") {
    my $i = @data;

    print "Format: Name,Phone,Marks1,Marks2,Marks3\nEnter details: ";
    my $input = <STDIN>;
    $input = trim("$input");
    my @linedata = split ',', $input;
    foreach my $j (0..4) {
        $linedata[$j] = trim("$linedata[$j]");
        $data[$i][$j] = $linedata[$j];
    }
} elsif ($command eq "edit") {
    if($index eq "all"){
        die "Index required to edit data.\n\n$help";
    }

    print "Current details:\n";
    printdata($data[$index]);

    print "Enter new details(fields left empty will not be updated):\n";
    my $input = <STDIN>;
    $input = trim("$input");
    my @linedata = split ',', $input;
    foreach my $j (0..4) {
        if(defined $linedata[$j]){
            $linedata[$j] = trim("$linedata[$j]");
            if($linedata[$j] ne "") {
                $data[$index][$j] = $linedata[$j];
            }
        }
    }
} else {
    print "$help";
}

open($students, '>', $file) or die "Could not open '$file'\n"; 
foreach my $s (@data) {
    print $students "$s->[0],$s->[1],$s->[2],$s->[3],$s->[4]\n";
}
