Name:           perl-Devel-StackTrace
Summary:        Perl module implementing stack trace and stack trace frame objects
Version:        2.03
Epoch:          1
Release:        2%{?dist}
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-StackTrace/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Devel-StackTrace-%{version}.tar.gz
BuildArch:      noarch

# --with release_tests ... also check "RELEASE_TESTS".
# Disabled by default
%bcond_with release_tests

# --with author_tests ... also check "AUTHOR_TESTS".
# Disabled by default
%bcond_with author_tests

BuildRequires:  perl-generators
BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%if %{with release_tests}
# for improved tests
BuildRequires:  perl(Exception::Class::Base)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod) > 1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Test::Pod::LinkCheck)
BuildRequires:  perl(Test::Pod::No404s)
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Test::Synopsis)
BuildRequires:  perl(LWP::Protocol::https)
%endif

%if %{with author_tests}
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod) > 1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Test::Spelling) >= 0.12
BuildRequires:  perl(Test::Synopsis)
# N/A in Fedora: BuildRequires:	perl(Code::TidyAll::Plugin::SortLines::Naturally) >= 0.000003
BuildRequires:  perl(Code::TidyAll::Plugin::Test::Vars) >= 0.02
BuildRequires:  perl(Parallel::ForkManager) >= 1.19
BuildRequires:  perl(Perl::Critic) >= 1.126
BuildRequires:  perl(Perl::Tidy) >= 20160302
BuildRequires:  perl(Test::CPAN::Meta::JSON) >= 0.16
BuildRequires:  perl(Test::Code::TidyAll) >= 0.50
BuildRequires:  perl(Test::Mojibake)
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Test::Vars) >= 0.009
BuildRequires:  perl(Test::Version) >= 2.05
%endif

%description
The Devel::StackTrace module contains two classes, Devel::StackTrace
and Devel::StackTraceFrame.  The goal of this object is to encapsulate
the information that can found through using the caller() function, as
well as providing a simple interface to this data.

The Devel::StackTrace object contains a set of Devel::StackTraceFrame
objects, one for each level of the stack.  The frames contain all the
data available from caller() as of Perl 5.6.0.

%prep
%setup -q -n Devel-StackTrace-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
%{__make} pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test %{?with_release_tests:RELEASE_TESTING=1} %{?with_author_tests:AUTHOR_TESTING=1}

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/Devel
%{_mandir}/man3/*

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:2.03-1
- Update to 2.03.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.02-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:2.02-1
- Update to 2.02.

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.01-2
- Perl 5.24 rebuild

* Fri Mar 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:2.01-1
- Update to 2.01.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:2.00-4
- Add %%license.
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.00-2
- Perl 5.22 rebuild

* Mon Nov 03 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:2,00-1
- Upstream update.
- Reflect upstream changes to BR:'s.

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.34-2
- Perl 5.20 rebuild

* Sat Jun 28 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.34-1
- Upstream update.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.32-1
- Upstream update.
- Activate AUTHOR_TESTING.
- Update BRs.

* Fri Jan 17 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.31-1
- Upstream update.
- Fix bogus %%changelog entry.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1:1.30-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.30-1
- Upstream update.
- Reflect new BR:'s.
- Modernize spec-file.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1:1.27-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.27-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.27-1
- Upstream update.

* Wed Nov 03 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.26-1
- Upstream update.

* Sun Sep 12 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.25-1
- Upstream update.
- Spec overhaul.
- Add %%bcond_with release_tests

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.22-5
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.22-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:1.22-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.22-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.20-2
- BR: perl(Test::Kwalitee).

* Sat Dec 13 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.20-1
- Upstream update.
- Bump epoch.

* Fri Aug 08 2008 Ralf Corsépius <rc040203@freenet.de> - 1.1902-1
- Upstream update.

* Wed Jun 25 2008 Ralf Corsépius <rc040203@freenet.de> - 1.1901-1
- Upstream update.

* Fri May 16 2008 Ralf Corsépius <rc040203@freenet.de> - 1.18-2
- Bump release.

* Mon Apr 07 2008 Ralf Corsépius <rc040203@freenet.de> - 1.18-1
- Upstream update.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.16-2
- Rebuild for perl 5.10 (again)

* Sun Feb 03 2008 Ralf Corsépius <rc040203@freenet.de> - 1.16-1
- Upstream update.
- Activate IS_MAINTAINER-tests.
- BR: perl(Test::Pod::Coverage).

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.15-3
- rebuild for new perl

* Wed Aug 29 2007 Ralf Corsépius <rc040203@freenet.de> - 1.15-2
- Update License.

* Mon Apr 30 2007 Ralf Corsépius <rc040203@freenet.de> - 1.15-1
- Upstream update.

* Sat Mar 17 2007 Ralf Corsépius <rc040203@freenet.de> - 1.14-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-2
- Mass rebuild.

* Tue Apr 04 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 1.12-2
- Rebuild for perl-5.8.8.

* Sun Oct 02 2005 Ralf Corsepius <rc040203@freenet.de> - 1.12-1
- Upstream update.
