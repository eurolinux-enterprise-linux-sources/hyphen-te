Name: hyphen-te
Summary: Telugu hyphenation rules
Epoch: 1
Version: 0.7.0
Release: 3%{?dist}
Source: http://download.savannah.gnu.org/releases/smc/hyphenation/patterns/%{name}-%{version}.tar.bz2
Group: Applications/Text
URL: http://wiki.smc.org.in
License: LGPLv3+
BuildArch: noarch
Requires: hyphen

%description
Telugu hyphenation rules.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_datadir}/hyphen
install -m644 -p *.dic %{buildroot}/%{_datadir}/hyphen

%files
%doc README COPYING ChangeLog
%{_datadir}/hyphen/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 29 2012 Parag <pnemade AT redhat DOT com> - 1:0.7.0-2
- Correct the changelog entry

* Tue Nov 27 2012 Parag <pnemade AT redhat DOT com> - 1:0.7.0-1
- Resolves:rh#880295- package does not follow naming guidelines

* Wed Nov 21 2012 Parag <pnemade AT redhat DOT com> - 0.20111229-2
- Add %%doc files

* Thu Aug 02 2012 Parag <pnemade AT redhat DOT com> - 0.20111229-1
- Update to new upstream 0.7.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100204-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100204-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100204-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 08 2010 Parag <pnemade AT redhat.com> - 0.20100204-1
- update to 20100204

* Thu Sep 24 2009 Parag <pnemade@redhat.com> - 0.20090924-1
- update to 20090924

* Mon Aug 17 2009 Parag <pnemade@redhat.com> - 0.20090813-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081213-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 06 2009 Caolan McNamara <caolanm@redhat.com> - 0.20081213-1
- initial version
