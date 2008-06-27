Summary:	SynCE - Synchronization engine
Summary(pl.UTF-8):	SynCE - silnik synchronizacji
Name:		synce-sync-engine
Version:	0.11.1
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/sync-engine-%{version}.tar.gz
# Source0-md5:	a552f4dad3dcd284821c1247054259a0
URL:		http://www.synce.org/
BuildRequires:	python
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
Requires:	libopensync-plugin-python >= 0.21
Requires:	python-dbus
Requires:	python-libxml2
Requires:	python-libxslt
Requires:	python-pygobject
Requires:	python-pyrapi2 >= %{version}
Requires:	python-pyrra >= %{version}
Requires:	python-pyrtfcomp >= 1.1
Requires:	python-setuptools
Requires:	synce-odccm >= %{version}
Requires:	synce-pywbxml >= 0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE - Synchronization engine.

%description -l pl.UTF-8
SynCE - silnik synchronizacji.

%prep
%setup -q -n sync-engine-%{version}

# Change python package path to normal on 'tools' folder
sed -i -e "#sys.path.insert(0,#d" tools/*.py

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG config/config.xml
%attr(755,root,root) %{_bindir}/clean_partnerships.py
%attr(755,root,root) %{_bindir}/configure_bindings.py
%attr(755,root,root) %{_bindir}/create_partnership.py
%attr(755,root,root) %{_bindir}/delete_partnership.py
%attr(755,root,root) %{_bindir}/list_partnerships.py
%attr(755,root,root) %{_bindir}/sync-engine
%attr(755,root,root) %{_bindir}/synce-install-plugins.py
%{py_sitescriptdir}/*.egg-info
%dir %{py_sitescriptdir}/SyncEngine
%dir %{py_sitescriptdir}/SyncEngine/formats
%dir %{py_sitescriptdir}/SyncEngine/formats/tzutils
%dir %{py_sitescriptdir}/SyncEngine/formats30
%dir %{py_sitescriptdir}/SyncEngine/formats30/tzutils
%dir %{py_sitescriptdir}/plugins
%{py_sitescriptdir}/SyncEngine/*.py[co]
%{py_sitescriptdir}/SyncEngine/formats/*.py[co]
%{py_sitescriptdir}/SyncEngine/formats/*.xsl
%{py_sitescriptdir}/SyncEngine/formats/tzutils/*.py[co]
%{py_sitescriptdir}/SyncEngine/formats30/*.py[co]
%{py_sitescriptdir}/SyncEngine/formats30/*.xsl
%{py_sitescriptdir}/SyncEngine/formats30/tzutils/*.py[co]
%{py_sitescriptdir}/plugins/*.py[co]
%dir %{py_sitescriptdir}/SyncEngine/wbxml
%{py_sitescriptdir}/SyncEngine/wbxml/*.py[co]
