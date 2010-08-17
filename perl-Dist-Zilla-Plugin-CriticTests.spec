%define upstream_name    Dist-Zilla-Plugin-CriticTests
%define upstream_version 1.102280

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Tests to check your code against best practices
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires: perl(English)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is an extension of the Dist::Zilla::Plugin::InlineFiles manpage,
providing the following files:

* * t/author/critic.t - a standard test to check your code against best
  practices

This plugin does not accept any option yet.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*
