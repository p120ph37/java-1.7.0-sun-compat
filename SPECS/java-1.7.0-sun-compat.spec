%define origin          sun
%define priority        1703
%define javaver         1.7.0
%define buildver        01
%define upstreamrel     fcs

%define name            java-%{javaver}-%{origin}-compat
%define version         %{javaver}%{?buildver:.%{buildver}}
%define release         1jpp
%define cname           java-%{javaver}-%{origin}

%define toplevel_dir    jdk%{javaver}%{?buildver:_%{buildver}}
%define sdklnk          java-%{javaver}-%{origin}
%define jrelnk          jre-%{javaver}-%{origin}
%define sdkdir          %{cname}-%{version}
%define jredir          %{sdkdir}/jre
%define sdkbindir       %{_jvmdir}/%{sdklnk}/bin
%define jrebindir       %{_jvmdir}/%{jrelnk}/bin
%define jvmjardir       %{_jvmjardir}/%{cname}-%{version}

%define x11encdirs      %{_datadir}/X11/fonts/encodings %{_prefix}/X11R6/lib/X11/fonts/encodings
%define fontconfigdir   %{_sysconfdir}/fonts
%define fontdir         %{_datadir}/fonts/java
%define xsldir          %{_datadir}/xml/%{name}-%{version}

%ifarch %{ix86} x86_64
%define has_javaws      1
%else
%define has_javaws      0
%endif
%define javaws_ver      %{javaver}

%ifarch %{ix86}
%define has_plugin      1
%else
%define has_plugin      0
%endif
%define pluginname      %{_jvmdir}/%{jredir}/plugin/i386/ns7/libjavaplugin_oji.so
# Browser packages (comma separated) for which we trigger plugin symlinking.
%define browserpkgs     mozilla, firefox, mozilla-firefox, opera, seamonkey
# Dirs where we manage plugin symlinks, no wildcards here.
%define plugindirs      %{_libdir}/mozilla/plugins

%define upstreamdir     %{_prefix}/java/%{toplevel_dir}

# Avoid manpage symlink breakage
%define __os_install_post %{nil}

# No debuginfo package needed here.
%define debug_package %{nil}

Name:           %{name}
Version:        %{version}
Release:        %{release}
Epoch:          0
Summary:        JPackage Java compatibility package for Sun's JDK
License:        JPackage License
Group:          Development/Interpreters
Vendor:         JPackage Project
Distribution:   JPackage
URL:            http://java.sun.com/javase/
Source1:        %{name}-register-java-fonts.xsl
Source2:        %{name}-unregister-java-fonts.xsl
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%ifarch %{ix86}
BuildArch:      i586
%endif

Provides:       java-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides:       jre-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides:       jre-%{origin} = %{epoch}:%{version}-%{release}
Provides:       jre-%{javaver}, java-%{javaver}, jre = %{epoch}:%{javaver}
Provides:       java-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java = %{epoch}:%{javaver} libjawt.so
Requires:       /usr/sbin/update-alternatives
# >= 1.7.3 for java 1.6.0 dirs
Requires:       jpackage-utils >= 0:1.7.3
BuildRequires:  jdk = 2000:%{javaver}%{?buildver:_%{buildver}}-%{upstreamrel}
Requires:       jdk = 2000:%{javaver}%{?buildver:_%{buildver}}-%{upstreamrel}
Requires(post): %{_bindir}/perl
Conflicts:      kaffe
BuildRequires:  jpackage-utils >= 0:1.5.38, sed
%if %{has_javaws}
Provides:       javaws = %{epoch}:%{javaws_ver}
%endif
Provides:       jndi = %{epoch}:%{version}, jndi-ldap = %{epoch}:%{version}
Provides:       jndi-cos = %{epoch}:%{version}, jndi-rmi = %{epoch}:%{version}
Provides:       jndi-dns = %{epoch}:%{version}
Provides:       jaas = %{epoch}:%{version}
Provides:       jsse = %{epoch}:%{version}
Provides:       jce = %{epoch}:%{version}
Provides:       jdbc-stdext = %{epoch}:3.0, jdbc-stdext = %{epoch}:%{version}
Provides:       java-sasl = %{epoch}:%{version}
# -devel
Provides:      java-%{javaver}-%{origin}-devel = %{epoch}:%{version}-%{release}
Provides:       java-sdk-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java-sdk-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java-sdk-%{javaver}, java-sdk = %{epoch}:%{javaver}
Provides:       java-devel-%{origin} = %{epoch}:%{version}-%{release}
Provides:       java-%{javaver}-devel, java-devel = %{epoch}:%{javaver}
# -src
Provides:       java-%{javaver}-%{origin}-src = %{epoch}:%{version}-%{release}
# -demo
Provides:       java-%{javaver}-%{origin}-demo = %{epoch}:%{version}-%{release}
# -plugin
%if %{has_plugin}
Provides:     java-%{javaver}-%{origin}-plugin = %{epoch}:%{version}-%{release}
Provides:       java-plugin = %{epoch}:%{javaver}
Provides:       java-%{javaver}-plugin = %{version}
Conflicts:      java-%{javaver}-ibm-plugin, java-%{javaver}-blackdown-plugin
Conflicts:      java-%{javaver}-bea-plugin
Obsoletes:      java-1.3.1-plugin, java-1.4.0-plugin, java-1.4.1-plugin
Obsoletes:      java-1.4.2-plugin, java-1.5.0-plugin, java-1.6.0-plugin
Requires(preun): %{_bindir}/find
%endif
# -fonts
Requires:       mktemp
Requires(preun): %{_bindir}/xsltproc
Requires(triggerin): %{_bindir}/xsltproc
Provides:      java-%{javaver}-%{origin}-fonts = %{epoch}:%{version}-%{release}
Provides:       java-fonts = %{javaver}, java-%{javaver}-fonts
Requires(postun): %{_bindir}/find
Conflicts:      java-%{javaver}-ibm-fonts, java-%{javaver}-blackdown-fonts
Conflicts:      java-%{javaver}-bea-fonts
Obsoletes:      java-1.3.1-fonts, java-1.4.0-fonts, java-1.4.1-fonts
Obsoletes:      java-1.4.2-fonts, java-1.5.0-fonts, java-1.6.0-fonts
# -alsa
Provides:       java-%{javaver}-%{origin}-alsa = %{epoch}:%{version}-%{release}
# -jdbc
Provides:       java-%{javaver}-%{origin}-jdbc = %{epoch}:%{version}-%{release}
#Requires:      %{_libdir}/libodbc.so, %{_libdir}/libodbcinst.so

%description
This package provides JPackage compatibility symlinks and directories
for the vendor's JDK rpm.


%prep
%setup -c -T


%build
# Nope.


%install
rm -rf $RPM_BUILD_ROOT %{name}-%{version}*.files

# main files
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
for i in %{upstreamdir}/* ; do
  f=$(basename $i)
  if [ ! -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/$f ] ; then
    ln -s $i $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
    echo "%{_jvmdir}/%{sdkdir}/$f" >> %{name}-%{version}-all.files
  fi
done

# native library paths
install -d -m 755 $RPM_BUILD_ROOT%{upstreamdir}/lib
%ifarch %{ix86}
ln -s %{_libdir} $RPM_BUILD_ROOT%{upstreamdir}/lib/i386
echo %{upstreamdir}/lib/i386 >> %{name}-%{version}-all.files
%else
%ifarch x86_64
install -d -m 755 $RPM_BUILD_ROOT%{upstreamdir}/lib/amd64_sun
echo "%%ghost %%dir %{upstreamdir}/lib/amd64_sun"
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}
echo "%%ghost %%dir %{_libdir}"
for i in %{upstreamdir}/lib/amd64/* ; do
  f=$(basename $i)
  ln -s %{upstreamdir}/lib/amd64_sun/$f $RPM_BUILD_ROOT%{_libdir}/$f
  echo %{_libdir}/$f >> %{name}-%{version}-all.files
done
%endif
%endif

# extensions handling
install -d -m 755 $RPM_BUILD_ROOT%{jvmjardir}
pushd $RPM_BUILD_ROOT%{jvmjardir}
   ln -s %{_jvmdir}/%{jredir}/lib/jsse.jar jsse-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/jce.jar jce-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jndi-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jndi-ldap-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jndi-cos-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jndi-rmi-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jaas-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar jdbc-stdext-%{version}.jar
   ln -s jdbc-stdext-%{version}.jar jdbc-stdext-3.0.jar
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar sasl-%{version}.jar
   for jar in *-%{version}.jar ; do
      [ "%{version}" = "%{javaver}" ] || \
         ln -fs $jar $(echo $jar | sed "s|-%{version}.jar|-%{javaver}.jar|g")
      ln -fs $jar $(echo $jar | sed "s|-%{version}.jar|.jar|g")
   done
popd

# rest of the jre
install -d -m 755 $RPM_BUILD_ROOT%{upstreamdir}/jre/lib/endorsed
ln -s %{upstreamdir}/jre/bin $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
%if %{has_plugin}
ln -s %{upstreamdir}/jre/plugin $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
%endif
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/fonts
install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security
for i in %{upstreamdir}/jre/* ; do
  test -e $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/`basename $i` || \
    ln -s $i $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
done
for i in %{upstreamdir}/jre/lib/* ; do
  test -e $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/`basename $i` || \
    ln -s $i $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib
done
for i in %{upstreamdir}/jre/lib/fonts/* ; do
  ln -s $i $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/fonts
done
for i in %{upstreamdir}/jre/lib/security/* ; do
  ln -s $i $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security
done

# jce policy file handling
install -d -m 755 $RPM_BUILD_ROOT%{_jvmprivdir}/%{cname}/jce/vanilla
for file in local_policy.jar US_export_policy.jar; do
  mv $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security/$file \
    $RPM_BUILD_ROOT%{_jvmprivdir}/%{cname}/jce/vanilla
  # for ghosts
  touch $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security/$file
done

# versionless symlinks
pushd $RPM_BUILD_ROOT%{_jvmdir}
ln -s %{jredir} %{jrelnk}
ln -s %{sdkdir} %{sdklnk}
popd

pushd $RPM_BUILD_ROOT%{_jvmjardir}
ln -s %{sdkdir} %{jrelnk}
ln -s %{sdkdir} %{sdklnk}
popd

# man pages
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
for manpage in %{upstreamdir}/man/man1/*; do
  ln -s $manpage $RPM_BUILD_ROOT%{_mandir}/man1/`basename $manpage .1`-%{name}.1
done

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/%{cname}
ln -s %{upstreamdir}/demo $RPM_BUILD_ROOT%{_libdir}/%{cname}

# font handling

pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir}/lib

   # Remove font.properties and use the system-wide one -- NiM
   rm -f font.properties
   ln -fs %{_sysconfdir}/java/font.properties .

   # remove supplied fonts.dir in preference of the one to be dynamically generated -- Rex
   rm fonts/fonts.dir

   # These %ghost'd files are created properly in %post  -- Rex
   touch fonts/{fonts.{alias,dir,scale,cache-1},XftCache,encodings.dir}

   if [ "%{fontdir}" != "%{jredir}/lib/fonts" ] ; then
      install -d -m 755 $RPM_BUILD_ROOT%{fontdir}
      mv fonts/* $RPM_BUILD_ROOT%{fontdir}
      rmdir fonts
      ln -fs %{fontdir} fonts
   fi

popd

# font registration/unregistration
install -d -m 755 $RPM_BUILD_ROOT%{xsldir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{xsldir}/register-java-fonts.xsl
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{xsldir}/unregister-java-fonts.xsl

find $RPM_BUILD_ROOT%{_jvmdir}/%{jredir} -type d \
  | sed 's|'$RPM_BUILD_ROOT'|%dir |' >> %{name}-%{version}-all.files
find $RPM_BUILD_ROOT%{_jvmdir}/%{jredir} -type f -o -type l \
  | sed 's|'$RPM_BUILD_ROOT'||'      >> %{name}-%{version}-all.files
cat %{name}-%{version}-all.files \
  | grep -v lib/fonts \
  | grep -v jre/lib/security \
  > %{name}-%{version}.files

%if %{has_plugin}
# plugin symlinks
for dir in %{plugindirs} ; do
  install -d -m 755 $RPM_BUILD_ROOT$dir
  ln -sf %{pluginname} $RPM_BUILD_ROOT$dir
  echo "%%ghost $dir/%(basename %{pluginname})" >> %{name}-%{version}.files
done
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%pre
# native library paths
%ifarch x86_64
mv %{upstreamdir}/lib/amd64 %{upstreamdir}/lib/amd64_sun
ln -s %{_libdir} %{upstreamdir}/lib/amd64
%endif


%preun
# fonts
[ $1 -eq 0 ] || exit 0
 # Unregister self in fontconfig aliases
if [ -w %{fontconfigdir}/fonts.conf ] ; then
   TMPFILE=$(/bin/mktemp -q /tmp/fonts.conf.XXXXXX) && \
   %{_bindir}/xsltproc --novalid %{xsldir}/unregister-java-fonts.xsl \
        %{fontconfigdir}/fonts.conf > $TMPFILE && \
   /bin/cat $TMPFILE > %{fontconfigdir}/fonts.conf && /bin/rm $TMPFILE
fi
%if %{has_plugin}
# plugin
{
  for dir in %{plugindirs} ; do
    [ -d "$dir" ] &&
      %{_bindir}/find "$dir" -lname %{pluginname} -print0 | xargs -0r rm -f
  done
} >/dev/null || :
%endif


%post
ext=
[ -f %{_mandir}/man1/java-%{name}.1.bz2 ] && ext=".bz2"
[ -f %{_mandir}/man1/java-%{name}.1.gz ] && ext=".gz"

update-alternatives --install %{_bindir}/java java %{jrebindir}/java %{priority} \
--slave %{_jvmdir}/jre                     jre                         %{_jvmdir}/%{jrelnk} \
--slave %{_jvmjardir}/jre                  jre_exports                 %{_jvmjardir}/%{jrelnk} \
%if %{has_plugin}
--slave %{_bindir}/jcontrol                jcontrol                    %{jrebindir}/jcontrol \
%endif
--slave %{_bindir}/keytool                 keytool                     %{jrebindir}/keytool \
--slave %{_bindir}/orbd                    orbd                        %{jrebindir}/orbd \
--slave %{_bindir}/pack200                 pack200                     %{jrebindir}/pack200 \
--slave %{_bindir}/policytool              policytool                  %{jrebindir}/policytool \
--slave %{_bindir}/rmid                    rmid                        %{jrebindir}/rmid \
--slave %{_bindir}/rmiregistry             rmiregistry                 %{jrebindir}/rmiregistry \
--slave %{_bindir}/servertool              servertool                  %{jrebindir}/servertool \
--slave %{_bindir}/tnameserv               tnameserv                   %{jrebindir}/tnameserv \
--slave %{_bindir}/unpack200               unpack200                   %{jrebindir}/unpack200 \
--slave %{_mandir}/man1/java.1$ext         java.1$ext                  %{_mandir}/man1/java-%{name}.1$ext \
--slave %{_mandir}/man1/keytool.1$ext      keytool.1$ext               %{_mandir}/man1/keytool-%{name}.1$ext \
--slave %{_mandir}/man1/orbd.1$ext         orbd.1$ext                  %{_mandir}/man1/orbd-%{name}.1$ext \
--slave %{_mandir}/man1/pack200.1$ext      pack200.1$ext               %{_mandir}/man1/pack200-%{name}.1$ext \
--slave %{_mandir}/man1/policytool.1$ext   policytool.1$ext            %{_mandir}/man1/policytool-%{name}.1$ext \
--slave %{_mandir}/man1/rmid.1$ext         rmid.1$ext                  %{_mandir}/man1/rmid-%{name}.1$ext \
--slave %{_mandir}/man1/rmiregistry.1$ext  rmiregistry.1$ext           %{_mandir}/man1/rmiregistry-%{name}.1$ext \
--slave %{_mandir}/man1/servertool.1$ext   servertool.1$ext            %{_mandir}/man1/servertool-%{name}.1$ext \
--slave %{_mandir}/man1/tnameserv.1$ext    tnameserv.1$ext             %{_mandir}/man1/tnameserv-%{name}.1$ext \
--slave %{_mandir}/man1/unpack200.1$ext    unpack200.1$ext             %{_mandir}/man1/unpack200-%{name}.1$ext \
%if %{has_javaws}
--slave %{_mandir}/man1/javaws.1$ext       javaws.1$ext                %{_mandir}/man1/javaws-%{name}.1$ext \
--slave %{_datadir}/javaws                 javaws                      %{_jvmdir}/%{jrelnk}/javaws
%endif

update-alternatives --install %{_jvmdir}/jre-%{origin} jre_%{origin} %{_jvmdir}/%{jrelnk} %{priority} \
--slave %{_jvmjardir}/jre-%{origin}        jre_%{origin}_exports     %{_jvmjardir}/%{jrelnk}

update-alternatives --install %{_jvmdir}/jre-%{javaver} jre_%{javaver} %{_jvmdir}/%{jrelnk} %{priority} \
--slave %{_jvmjardir}/jre-%{javaver}       jre_%{javaver}_exports      %{_jvmjardir}/%{jrelnk}

if [ -d %{_jvmdir}/%{jrelnk}/lib/security ]; then
  # Need to remove the old jars in order to support upgrading, ugly :(
  # update-alternatives fails silently if the link targets exist as files.
  rm -f %{_jvmdir}/%{jrelnk}/lib/security/{local,US_export}_policy.jar
fi
update-alternatives \
  --install \
    %{_jvmdir}/%{jrelnk}/lib/security/local_policy.jar \
    jce_%{javaver}_%{origin}_local_policy \
    %{_jvmprivdir}/%{cname}/jce/vanilla/local_policy.jar \
    %{priority} \
  --slave \
    %{_jvmdir}/%{jrelnk}/lib/security/US_export_policy.jar \
    jce_%{javaver}_%{origin}_us_export_policy \
    %{_jvmprivdir}/%{cname}/jce/vanilla/US_export_policy.jar
  
%{_bindir}/perl -p -i -e 's|^.*application/x-java-jnlp-file.*||' %{_sysconfdir}/mailcap 2>/dev/null
echo "type=application/x-java-jnlp-file; description=\"Java Web Start\"; exts=\"jnlp\"" >> %{_sysconfdir}/mailcap 2>/dev/null

%{_bindir}/perl -p -i -e 's|^.*application/x-java-jnlp-file.*||' %{_sysconfdir}/mime.types 2>/dev/null
echo "application/x-java-jnlp-file      jnlp" >> %{_sysconfdir}/mime.types 2>/dev/null

# devel
update-alternatives --install %{_bindir}/javac javac %{sdkbindir}/javac %{priority} \
--slave %{_jvmdir}/java                     java_sdk                    %{_jvmdir}/%{sdklnk} \
--slave %{_jvmjardir}/java                  java_sdk_exports            %{_jvmjardir}/%{sdklnk} \
--slave %{_bindir}/appletviewer             appletviewer                %{sdkbindir}/appletviewer \
--slave %{_bindir}/apt                      apt                         %{sdkbindir}/apt \
--slave %{_bindir}/extcheck                 extcheck                    %{sdkbindir}/extcheck \
--slave %{_bindir}/HtmlConverter            HtmlConverter               %{sdkbindir}/HtmlConverter \
--slave %{_bindir}/idlj                     idlj                        %{sdkbindir}/idlj \
--slave %{_bindir}/jar                      jar                         %{sdkbindir}/jar \
--slave %{_bindir}/jarsigner                jarsigner                   %{sdkbindir}/jarsigner \
--slave %{_bindir}/javadoc                  javadoc                     %{sdkbindir}/javadoc \
--slave %{_bindir}/javah                    javah                       %{sdkbindir}/javah \
--slave %{_bindir}/javap                    javap                       %{sdkbindir}/javap \
--slave %{_bindir}/jconsole                 jconsole                    %{sdkbindir}/jconsole \
--slave %{_bindir}/jdb                      jdb                         %{sdkbindir}/jdb \
--slave %{_bindir}/jhat                     jhat                        %{sdkbindir}/jhat \
--slave %{_bindir}/jinfo                    jinfo                       %{sdkbindir}/jinfo \
--slave %{_bindir}/jmap                     jmap                        %{sdkbindir}/jmap \
--slave %{_bindir}/jps                      jps                         %{sdkbindir}/jps \
--slave %{_bindir}/jrunscript               jrunscript                  %{sdkbindir}/jrunscript \
--slave %{_bindir}/jsadebugd                jsadebugd                   %{sdkbindir}/jsadebugd \
--slave %{_bindir}/jstack                   jstack                      %{sdkbindir}/jstack \
--slave %{_bindir}/jstat                    jstat                       %{sdkbindir}/jstat \
--slave %{_bindir}/jstatd                   jstatd                      %{sdkbindir}/jstatd \
--slave %{_bindir}/native2ascii             native2ascii                %{sdkbindir}/native2ascii \
--slave %{_bindir}/rmic                     rmic                        %{sdkbindir}/rmic \
--slave %{_bindir}/schemagen                schemagen                   %{sdkbindir}/schemagen \
--slave %{_bindir}/serialver                serialver                   %{sdkbindir}/serialver \
--slave %{_bindir}/wsgen                    wsgen                       %{sdkbindir}/wsgen \
--slave %{_bindir}/wsimport                 wsimport                    %{sdkbindir}/wsimport \
--slave %{_bindir}/xjc                      xjc                         %{sdkbindir}/xjc \
--slave %{_mandir}/man1/appletviewer.1$ext  appletviewer.1$ext          %{_mandir}/man1/appletviewer-%{name}.1$ext \
--slave %{_mandir}/man1/apt.1$ext           apt.1$ext                   %{_mandir}/man1/apt-%{name}.1$ext \
--slave %{_mandir}/man1/extcheck.1$ext      extcheck.1$ext              %{_mandir}/man1/extcheck-%{name}.1$ext \
--slave %{_mandir}/man1/idlj.1$ext          idlj.1$ext                  %{_mandir}/man1/idlj-%{name}.1$ext \
--slave %{_mandir}/man1/jar.1$ext           jar.1$ext                   %{_mandir}/man1/jar-%{name}.1$ext \
--slave %{_mandir}/man1/jarsigner.1$ext     jarsigner.1$ext             %{_mandir}/man1/jarsigner-%{name}.1$ext \
--slave %{_mandir}/man1/javac.1$ext         javac.1$ext                 %{_mandir}/man1/javac-%{name}.1$ext \
--slave %{_mandir}/man1/javadoc.1$ext       javadoc.1$ext               %{_mandir}/man1/javadoc-%{name}.1$ext \
--slave %{_mandir}/man1/javah.1$ext         javah.1$ext                 %{_mandir}/man1/javah-%{name}.1$ext \
--slave %{_mandir}/man1/javap.1$ext         javap.1$ext                 %{_mandir}/man1/javap-%{name}.1$ext \
--slave %{_mandir}/man1/jconsole.1$ext      jconsole.1$ext              %{_mandir}/man1/jconsole-%{name}.1$ext \
--slave %{_mandir}/man1/jdb.1$ext           jdb.1$ext                   %{_mandir}/man1/jdb-%{name}.1$ext \
--slave %{_mandir}/man1/jhat.1$ext          jhat.1$ext                  %{_mandir}/man1/jhat-%{name}.1$ext \
--slave %{_mandir}/man1/jinfo.1$ext         jinfo.1$ext                 %{_mandir}/man1/jinfo-%{name}.1$ext \
--slave %{_mandir}/man1/jmap.1$ext          jmap.1$ext                  %{_mandir}/man1/jmap-%{name}.1$ext \
--slave %{_mandir}/man1/jps.1$ext           jps.1$ext                   %{_mandir}/man1/jps-%{name}.1$ext \
--slave %{_mandir}/man1/jrunscript.1$ext    jrunscript.1$ext            %{_mandir}/man1/jrunscript-%{name}.1$ext \
--slave %{_mandir}/man1/jsadebugd.1$ext     jsadebugd.1$ext             %{_mandir}/man1/jsadebugd-%{name}.1$ext \
--slave %{_mandir}/man1/jstack.1$ext        jstack.1$ext                %{_mandir}/man1/jstack-%{name}.1$ext \
--slave %{_mandir}/man1/jstat.1$ext         jstat.1$ext                 %{_mandir}/man1/jstat-%{name}.1$ext \
--slave %{_mandir}/man1/jstatd.1$ext        jstatd.1$ext                %{_mandir}/man1/jstatd-%{name}.1$ext \
--slave %{_mandir}/man1/native2ascii.1$ext  native2ascii.1$ext          %{_mandir}/man1/native2ascii-%{name}.1$ext \
--slave %{_mandir}/man1/rmic.1$ext          rmic.1$ext                  %{_mandir}/man1/rmic-%{name}.1$ext \
--slave %{_mandir}/man1/schemagen.1$ext     schemagen.1$ext             %{_mandir}/man1/schemagen-%{name}.1$ext \
--slave %{_mandir}/man1/serialver.1$ext     serialver.1$ext             %{_mandir}/man1/serialver-%{name}.1$ext \
--slave %{_mandir}/man1/wsgen.1$ext         wsgen.1$ext                 %{_mandir}/man1/wsgen-%{name}.1$ext \
--slave %{_mandir}/man1/wsimport.1$ext      wsimport.1$ext              %{_mandir}/man1/wsimport-%{name}.1$ext \
--slave %{_mandir}/man1/xjc.1$ext           xjc.1$ext                   %{_mandir}/man1/xjc-%{name}.1$ext

update-alternatives --install %{_jvmdir}/java-%{origin} java_sdk_%{origin} %{_jvmdir}/%{sdklnk} %{priority} \
--slave %{_jvmjardir}/java-%{origin}        java_sdk_%{origin}_exports     %{_jvmjardir}/%{sdklnk}

update-alternatives --install %{_jvmdir}/java-%{javaver} java_sdk_%{javaver} %{_jvmdir}/%{sdklnk} %{priority} \
--slave %{_jvmjardir}/java-%{javaver}       java_sdk_%{javaver}_exports      %{_jvmjardir}/%{sdklnk}

# fonts
# We do not care if all/any of this actually succeeds
# Therefore errors are catched but messages allowed
{
    # Legacy font handling

    if [ -x %{_bindir}/ttmkfdir ] ; then
      %{_bindir}/ttmkfdir -d %{fontdir} -o %{fontdir}/fonts.scale
      # Mandrake workaround
      %{_bindir}/perl -pi -e 's@0-c-0@0-p-0@g' %{fontdir}/fonts.scale
    fi

    for edir in %{x11encdirs} ; do
        [ ! -d $edir ] || \
            mkfontdir -e $edir -e $edir/large %{fontdir} || :
    done

    [ -x %{_sbindir}/chkfontpath ] && %{_sbindir}/chkfontpath -q -a %{fontdir}

    # The following commands will be executed on upgrade by their respective
    # packages

    # Late legacy font handling
    if [ -x %{_bindir}/redhat-update-gnome-font-install ] ; then
        %{_bindir}/redhat-update-gnome-font-install
    fi

    if [ -x %{_bindir}/redhat-update-gnome-font-install2 ] ; then
        %{_bindir}/redhat-update-gnome-font-install2
    fi

    # Modern font handling
    if [ -x %{_bindir}/fc-cache ] ; then
        %{_bindir}/fc-cache -f %{_datadir}/fonts
    fi
} || :


%if %{has_plugin}
%triggerin -- %{browserpkgs}
{
  for dir in %{plugindirs} ; do
    [ -d "$dir" -a -e %{pluginname} ] && ln -sf %{pluginname} "$dir"
  done
} >/dev/null || :
%endif


%triggerin -- fontconfig, %{fontconfigdir}/fonts.conf
# fonts
TMPFILE=$(/bin/mktemp -q /tmp/fonts.conf.XXXXXX) && \
%{_bindir}/xsltproc --novalid %{xsldir}/register-java-fonts.xsl \
   %{fontconfigdir}/fonts.conf > $TMPFILE && \
/bin/cat $TMPFILE > %{fontconfigdir}/fonts.conf && /bin/rm $TMPFILE


%postun
[ $1 -eq 0 ] || exit 0
# main
update-alternatives --remove java %{jrebindir}/java
update-alternatives --remove \
  jce_%{javaver}_%{origin}_local_policy \
  %{_jvmprivdir}/%{cname}/jce/vanilla/local_policy.jar
update-alternatives --remove jre_%{origin}  %{_jvmdir}/%{jrelnk}
update-alternatives --remove jre_%{javaver} %{_jvmdir}/%{jrelnk}

# devel
update-alternatives --remove javac %{sdkbindir}/javac
update-alternatives --remove java_sdk_%{origin}  %{_jvmdir}/%{sdklnk}
update-alternatives --remove java_sdk_%{javaver} %{_jvmdir}/%{sdklnk}

# fonts
# We do not care if all/any of this actually succeeds
# Therefore errors are catched but messages allowed
{
   # Rehash the font dir to keep only stuff manually installed

   if [ -d %{fontdir} ] && [ $(%{_bindir}/find %{fontdir} \
        -follow -type f -iname "*.ttf" -printf "\b\b\b\btrue") ] ; then

        if [ -x %{_bindir}/ttmkfdir ] ; then
          %{_bindir}/ttmkfdir -d %{fontdir} -o %{fontdir}/fonts.scale
        fi

        for edir in %{x11encdirs} ; do
            [ ! -d $edir ] || \
                mkfontdir -e $edir -e $edir/large %{fontdir} || :
        done

   elif [ -x %{_sbindir}/chkfontpath ] ; then
        %{_sbindir}/chkfontpath -q -r %{fontdir}
   fi

   if [ -x %{_bindir}/redhat-update-gnome-font-install ] ; then
        %{_bindir}/redhat-update-gnome-font-install
   fi

   if [ -x %{_bindir}/redhat-update-gnome-font-install2 ] ; then
        %{_bindir}/redhat-update-gnome-font-install2
   fi

   if [ -x %{_bindir}/fc-cache ] ; then
        %{_bindir}/fc-cache -f %{_datadir}/fonts
   fi

} || :

# native library paths
%ifarch x86_64
rm %{upstreamdir}/lib/amd64
mv %{upstreamdir}/lib/amd64_sun %{upstreamdir}/lib/amd64
%endif


%files -f %{name}-%{version}.files
%defattr(-,root,root,-)
%dir %{upstreamdir}/jre/lib/endorsed
%dir %{_jvmdir}/%{sdkdir}
%dir %{jvmjardir}
%{_jvmdir}/%{jredir}/lib/fonts
%dir %{_jvmdir}/%{jredir}/lib/security
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/cacerts
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.security
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/blacklist
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/trusted.libraries
%if %{has_javaws}
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/javaws.policy
%endif
%ghost %{_jvmdir}/%{jredir}/lib/security/local_policy.jar
%ghost %{_jvmdir}/%{jredir}/lib/security/US_export_policy.jar
%{jvmjardir}/*.jar
%{_jvmdir}/%{jrelnk}
%{_jvmjardir}/%{jrelnk}
%{_jvmprivdir}/*
# Note: no trailing wildcards on man pages on purpose
%{_mandir}/man1/*-%{name}.1
%{_jvmdir}/%{sdklnk}
%{_jvmjardir}/%{sdklnk}
%{_libdir}/%{cname}
%dir %{fontdir}
%dir %{xsldir}
%{fontdir}/*.ttf
%{xsldir}/*.xsl
%config(noreplace) %{fontdir}/fonts.alias
%ghost %{fontdir}/fonts.dir
%ghost %{fontdir}/fonts.scale
%ghost %{fontdir}/fonts.cache-1
%ghost %{fontdir}/XftCache
%ghost %{fontdir}/encodings.dir


%changelog
* Tue Nov 15 2011 Aaron Wirtz <github.com/p120ph37> - 0:1.7.0.01-1jpp
- 1.7.0_01.

* Sat Oct  6 2007 Ville Skyttä <scop at jpackage.org> - 0:1.6.0.03-1jpp
- 1.6.0_03.

* Wed Jul  4 2007 Ville Skyttä <scop at jpackage.org> - 0:1.6.0.02-1jpp
- 1.6.0_02.

* Mon Apr  2 2007 Ville Skyttä <scop at jpackage.org> - 0:1.6.0.01-1jpp
- 1.6.0_01.

* Mon Dec 11 2006 Ville Skyttä <scop at jpackage.org> - 0:1.6.0-1jpp
- 1.6.0.

* Sat Nov 11 2006 Ville Skyttä <scop at jpackage.org> - 0:1.6.0-0.1.rc.1jpp
- 1.6.0-rc, based on 1.5.0.09-1jpp.
- Drop hard dependency on chkfontpath and ttmkfdir, handle missing mkfontdir.
- Move demo symlinks to %%{_libdir}, contains arch dependent files.
- Fix jvm-exports symlinks with _XX-less java versions.
- Improve scriptlet dependencies.
- Change to arch specific.
