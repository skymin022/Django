public class Encoding implements Filter {
    private String encoding

    @override
        public void init (FilterConfig filterConfig) throws ServletExceoption {
            encoding - filterConfig.getInitParameter("encoding")
        }

    @override
    public void doFilter(ServletRequest request, ServletResponse response, F)




}