Summary:	An audio control application for Linux/SPARC
Name:		audioctl
Version:	1.3
Release:	%mkrel 5
License:	BSD
Group:		Sound
Source0:	ftp://ftp.dementia.org/pub/linux/sparc/audio/%{name}-%{version}.tar.bz2
ExclusiveArch:	sparc sparcv9 sparc64

%description
audioctl displays or sets various audio system driver variables.
It can be used to change such audio parameters as volume, sampling
rate, and output device.

%prep
%setup -q -n %{name}

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m644 %{name}.1  -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

