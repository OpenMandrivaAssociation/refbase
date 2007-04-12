%define 	name refbase
%define		version 0.9.0
%define		release %mkrel 1

Summary: 	Web-based, multi-user interface for managing scientific literature & citations

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://prdownloads.sourceforge.net/refbase/%{name}-%{version}.tar.bz2

License:	GPL
Group:		System/Servers
Url:		http://refbase.sourceforge.net

Requires:	bibutils
Requires:	MySQL
Requires:	mod_php
Requires:	php-mysql
Requires:	webserver

BuildArch:	noarch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
refbase is a web-based, standards-compliant, multi-user interface 
for managing scientific literature & bibliographic references.
Based on php & mysql, it offers a bibliography database with 
powerful search tools and automatically generated citation lists.

To finish the installation, follow the procedure located in
%{var}/www/html/%{name}/INSTALL

%prep
%setup -q

%build

%install
%{__rm} -rf  %{buildroot}/

# install files
install -d -m 755  %{buildroot}/%{_var}/www/html/%{name}
perl -pi -e 's|/usr/local/mysql/bin/mysql|"%{_bindir}/mysql"|;' install.php
cp -pRH *  %{buildroot}/%{_var}/www/html/%{name}
chmod 644  %{buildroot}/%{_var}/www/html/%{name}/install.sql
chmod 644  %{buildroot}/%{_var}/www/html/%{name}/contrib/endnote/endnote2mysql.php

%clean
rm -rf  %{buildroot}/

#%post

#%postun

%files
%defattr(-,root,root,0755)
%{_var}/www/html/%{name}/*
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO UPDATE


