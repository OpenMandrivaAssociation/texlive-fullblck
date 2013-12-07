# revision 25434
# category Package
# catalog-ctan /macros/latex/contrib/fullblck
# catalog-date 2008-09-12 11:36:07 +0200
# catalog-license lppl
# catalog-version 1.03
Name:		texlive-fullblck
Version:	1.03
Release:	7
Summary:	Left-blocking for letter class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fullblck
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Used with the letter documentclass to set the letter in a
fullblock style (everything at the left margin).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fullblck/fullblck.sty
%doc %{_texmfdistdir}/doc/latex/fullblck/README
%doc %{_texmfdistdir}/doc/latex/fullblck/fullblck.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fullblck/fullblck.dtx
%doc %{_texmfdistdir}/source/latex/fullblck/fullblck.dtx.asc
%doc %{_texmfdistdir}/source/latex/fullblck/fullblck.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.03-3
+ Revision: 779462
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.03-2
+ Revision: 752159
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.03-1
+ Revision: 718513
- texlive-fullblck
- texlive-fullblck
- texlive-fullblck
- texlive-fullblck

