# revision 20333
# category Package
# catalog-ctan /macros/latex/contrib/smalltableof
# catalog-date 2010-11-05 12:10:03 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-smalltableof
Version:	20101105
Release:	6
Summary:	Create listoffigures etc. in a single chapter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/smalltableof
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smalltableof.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smalltableof.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows you to create a list of figures and list of
tables in a chapter named 'List' that contains separate
sections for each list of figures, tables, etc.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/smalltableof/smalltableof.sty
%doc %{_texmfdistdir}/doc/latex/smalltableof/README
%doc %{_texmfdistdir}/doc/latex/smalltableof/smalltableof-doc-fr.pdf
%doc %{_texmfdistdir}/doc/latex/smalltableof/smalltableof-doc-fr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101105-2
+ Revision: 756070
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101105-1
+ Revision: 719552
- texlive-smalltableof
- texlive-smalltableof
- texlive-smalltableof
- texlive-smalltableof

