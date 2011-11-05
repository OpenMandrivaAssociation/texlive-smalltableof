# revision 20333
# category Package
# catalog-ctan /macros/latex/contrib/smalltableof
# catalog-date 2010-11-05 12:10:03 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-smalltableof
Version:	20101105
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package allows you to create a list of figures and list of
tables in a chapter named 'List' that contains separate
sections for each list of figures, tables, etc.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/smalltableof/smalltableof.sty
%doc %{_texmfdistdir}/doc/latex/smalltableof/README
%doc %{_texmfdistdir}/doc/latex/smalltableof/smalltableof-doc-fr.pdf
%doc %{_texmfdistdir}/doc/latex/smalltableof/smalltableof-doc-fr.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
