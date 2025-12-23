#!/usr/bin/env perl
use v5.42;
use List::Util qw(sum);

for my $n (100..999) {
    say $n if $n == sum map {$_ ** 3} split //, $n;
}
