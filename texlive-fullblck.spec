# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fullblck
# catalog-date 2008-09-12 11:36:07 +0200
# catalog-license lppl
# catalog-version 1.03
Name:		texlive-fullblck
Version:	1.03
Release:	2
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

%description
Used with the letter documentclass to set the letter in a
fullblock style (everything at the left margin).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/fullblck/README
%doc %{_texmfdistdir}/doc/latex/fullblck/fullblck.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fullblck/fullblck.dtx
%doc %{_texmfdistdir}/source/latex/fullblck/fullblck.dtx.asc

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc source %{buildroot}%{_texmfdistdir}
