#!/usr/bin/perl
use strict;
use warnings;
use autodie;

print "ok";


sub choose {
    my($n, @data) = @_;    # 需要从 @data 中取出 $n 项
    my @result;
    return [map {[$_]} @data] if $n == 1;  # 只取一个时用
    while (1) {
        last if @data < $n; # 退出条件
        my $item = shift @data;
        my $ret = choose($n-1, @data);
        for (@$ret) {
            unshift @$_, $item;
            push @result, $_;
        }
    }

    return \@result;
}


local $, = ' ';
for (@{choose 3, 1 .. 8}) {
    print @$_;
	print "\n";
}



