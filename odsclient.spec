Summary:	Free dynamic DNS services
Summary(pl):	Darmowy serwis DNS
Name:		odsclient
Version:	1.02
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ods.org/%{name}-%{version}.tar.gz
URL:		http://www.ods.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ODS provides free dynamic DNS services (e.g. a host such as
yourhost.ods.org pointing to your computer) with a wide selection of
domains.

%description -l pl
ODS prowadzi darmowy serwis DNS z szerokim wachlarzem dostêpnych
domen.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
