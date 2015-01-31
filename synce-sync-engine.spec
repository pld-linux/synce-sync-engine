# TODO
# - move (to private dir) or rename .py files in bindir not to be so generic
#
# Conditional build:
%bcond_without	opensync0_2x	# OpenSync 0.2x (opensync02) plugin
%bcond_without	opensync0_3x	# OpenSync 0.3x plugin
#
Summary:	SynCE - Synchronization engine
Summary(pl.UTF-8):	SynCE - silnik synchronizacji
Name:		synce-sync-engine
Version:	0.16
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	92a9b81cba6c820f2639c50d79b6fd0d
URL:		http://www.synce.org/
BuildRequires:	python
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-dbus
Requires:	python-libxml2
Requires:	python-libxslt
Requires:	python-pygobject
Requires:	python-pyrapi2 >= 0.12
Requires:	python-pyrra >= 0.12
Requires:	python-pyrtfcomp >= 1.1
Requires:	python-setuptools
Requires:	synce-core
#Requires:	synce-pywbxml >= 0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE - Synchronization engine.

%description -l pl.UTF-8
SynCE - silnik synchronizacji.

%package -n libopensync-plugin-synce
Summary:	SynCE plugin for OpenSync framework
Summary(pl.UTF-8):	Wtyczka SynCE dla szkieletu OpenSync
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	libopensync-plugin-python >= 0.30
Requires:	python-opensync >= 1:0.39-7

%description -n libopensync-plugin-synce
SynCE plugin for OpenSync framework.

%description -n libopensync-plugin-synce -l pl.UTF-8
Wtyczka SynCE dla szkieletu OpenSync.

%package -n libopensync02-plugin-synce
Summary:	SynCE plugin for OpenSync 0.2x framework
Summary(pl.UTF-8):	Wtyczka SynCE dla szkieletu OpenSync 0.2x
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	libopensync02-plugin-python >= 0.20
Requires:	python-opensync02 >= 0.20

%description -n libopensync02-plugin-synce
SynCE plugin for OpenSync 0.2x framework.

%description -n libopensync02-plugin-synce -l pl.UTF-8
Wtyczka SynCE dla szkieletu OpenSync 0.2x.

%prep
%setup -q

# Change python package path to normal on 'tools' folder
%{__sed} -i -e "/^sys\.path\.insert(0,/d" tools/*.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

#install -d $RPM_BUILD_ROOT%{_datadir}/libopensync1/python-plugins
#install -Dp plugins/synce-opensync-plugin-3x.py $RPM_BUILD_ROOT%{_datadir}/libopensync1/python-plugins
install -Dp config/org.synce.SyncEngine.service $RPM_BUILD_ROOT%{_datadir}/dbus-1/services/org.synce.SyncEngine.service
install -Dp config/syncengine.conf.xml $RPM_BUILD_ROOT%{_sysconfdir}/syncengine.conf.xml

# do the job on packaging stage
%if %{with opensync0_3x}
install -d $RPM_BUILD_ROOT%{_datadir}/libopensync1/python-plugins
%{__mv} $RPM_BUILD_ROOT%{py_sitescriptdir}/plugins/synce-opensync-plugin-3x.py* $RPM_BUILD_ROOT%{_datadir}/libopensync1/python-plugins
%else
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/plugins/synce-opensync-plugin-3x.py*
%endif
%if %{with opensync0_2x}
install -d $RPM_BUILD_ROOT%{_libdir}/opensync/python-plugins
%{__mv} $RPM_BUILD_ROOT%{py_sitescriptdir}/plugins/synce-opensync-plugin-2x.py* $RPM_BUILD_ROOT%{_libdir}/opensync/python-plugins
%else
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/plugins/synce-opensync-plugin-2x.py*
%endif
%{__rm} $RPM_BUILD_ROOT%{_bindir}/synce-install-plugins.py
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/plugins/__init__.py*
rmdir $RPM_BUILD_ROOT%{py_sitescriptdir}/plugins

%{__rm} $RPM_BUILD_ROOT%{_docdir}/sync-engine/org.synce.SyncEngine.service
%{__rm} $RPM_BUILD_ROOT%{_docdir}/sync-engine/syncengine.conf.xml

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/syncengine.conf.xml
%attr(755,root,root) %{_bindir}/clean_partnerships.py
%attr(755,root,root) %{_bindir}/configure_bindings.py
%attr(755,root,root) %{_bindir}/create_partnership.py
%attr(755,root,root) %{_bindir}/delete_partnership.py
%attr(755,root,root) %{_bindir}/list_partnerships.py
%attr(755,root,root) %{_bindir}/sync-engine
%{_datadir}/dbus-1/services/org.synce.SyncEngine.service

%dir %{py_sitescriptdir}/SyncEngine
%{py_sitescriptdir}/SyncEngine/*.py[co]
%dir %{py_sitescriptdir}/SyncEngine/formats
%{py_sitescriptdir}/SyncEngine/formats/*.py[co]
%{py_sitescriptdir}/SyncEngine/formats/*.xsl
%dir %{py_sitescriptdir}/SyncEngine/formats/tzutils
%{py_sitescriptdir}/SyncEngine/formats/tzutils/*.py[co]
%dir %{py_sitescriptdir}/SyncEngine/formats30
%{py_sitescriptdir}/SyncEngine/formats30/*.py[co]
%{py_sitescriptdir}/SyncEngine/formats30/*.xsl
%dir %{py_sitescriptdir}/SyncEngine/formats30/tzutils
%{py_sitescriptdir}/SyncEngine/formats30/tzutils/*.py[co]
%dir %{py_sitescriptdir}/SyncEngine/wbxml
%{py_sitescriptdir}/SyncEngine/wbxml/*.py[co]
%{py_sitescriptdir}/sync_engine-%{version}-py*.egg-info

%if %{with opensync0_2x}
%files -n libopensync02-plugin-synce
%defattr(644,root,root,755)
%{_libdir}/opensync/python-plugins/synce-opensync-plugin-2x.py*
%endif

%if %{with opensync0_3x}
%files -n libopensync-plugin-synce
%defattr(644,root,root,755)
%doc plugins/synce-opensync-plugin-3x.README
%{_datadir}/libopensync1/python-plugins/synce-opensync-plugin-3x.py*
%endif
