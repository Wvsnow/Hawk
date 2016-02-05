#!/usr/bin/perl
use strict;
use warnings;
use autodie;

print "ok";


sub choose {
    my($n, @data) = @_;    # ��Ҫ�� @data ��ȡ�� $n ��
    my @result;
    return [map {[$_]} @data] if $n == 1;  # ֻȡһ��ʱ��
    while (1) {
        last if @data < $n; # �˳�����
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



