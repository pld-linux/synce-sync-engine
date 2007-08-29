Summary:	SynCE - Synchronization engine
Name:		synce-sync-engine
Version:	0.10.0
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	aa70ab8804c0d981e84963010852d3c5
URL:		http://www.synce.org/
BuildRequires:	libopensync-plugin-python >= 0.21
BuildRequires:	libxml2
BuildRequires:	libxslt
BuildRequires:	python-dbus
BuildRequires:	python-pygobject
#BuildRequires:	python-pyxml
BuildRequires:	sed >= 4.0
BuildRequires:	synce-librtfcomp-devel >= 1.1
BuildRequires:	synce-odccm >= 0.10.0
BuildRequires:	synce-pywbxml-devel >= 0.1
BuildRequires:	synce-rra >= 0.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q

# Change python package path to normal on 'tools' folder
sed -i -e "#sys.path.insert(0,#d" tools/*.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{py_sitedir},%{_libdir}/%{name}/python-plugins}
install sync-engine $RPM_BUILD_ROOT%{_bindir}
install tools/*.py $RPM_BUILD_ROOT%{_bindir}
cp -a engine/* $RPM_BUILD_ROOT%{py_sitedir}
cp -a config.xml $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a tests $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a opensync-plugin.py $RPM_BUILD_ROOT%{_libdir}/%{name}/python-plugins/synce.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_bindir}/clean_partnerships.py
%attr(755,root,root) %{_bindir}/create_partnership.py
%attr(755,root,root) %{_bindir}/delete_partnership.py
%attr(755,root,root) %{_bindir}/do_sync.py
%attr(755,root,root) %{_bindir}/list_partnerships.py
%attr(755,root,root) %{_bindir}/select_partnership.py
%attr(755,root,root) %{_bindir}/sync-engine
%{_datadir}/synce-sync-engine
%{_libdir}/synce-sync-engine
%{py_sitedir}/*.py
%{py_sitedir}/formats
