#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Tee
Version  : 0.65
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/IO-Tee-0.65.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/IO-Tee-0.65.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-tee-perl/libio-tee-perl_0.65-1.debian.tar.xz
Summary  : 'Multiplex output to multiple output handles'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-Tee-license
Requires: perl-IO-Tee-man

%description
Perl 5 module IO::Tee
Lingua::Stem::Ru is a pure perl module that lets you multiplex output
to multiple file handles.

%package license
Summary: license components for the perl-IO-Tee package.
Group: Default

%description license
license components for the perl-IO-Tee package.


%package man
Summary: man components for the perl-IO-Tee package.
Group: Default

%description man
man components for the perl-IO-Tee package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n IO-Tee-0.65
mkdir -p %{_topdir}/BUILD/IO-Tee-0.65/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/IO-Tee-0.65/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-IO-Tee
cp LICENSE %{buildroot}/usr/share/doc/perl-IO-Tee/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/IO/Tee.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-IO-Tee/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Tee.3
