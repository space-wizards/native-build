#include <glib.h>
#include <stdlib.h>

G_DEFINE_QUARK (g_convert_error, g_convert_error)

// gmessages
gchar * g_convert_with_fallback(const gchar * str, gssize u0, const gchar * u1, const gchar * u2, const gchar * u3, gsize * u4, gsize * u5, GError ** u6) {
	return NULL;
}
int g_strcmp0(const gchar * a, const gchar * b) {
	// fix this if there's any user that cares about ordering
	return (a && b) ? strcmp(a, b) : 1;
}
int g_pattern_match_simple(const gchar * a, const gchar * b) {
	// part of 'expected messages' stuff - how exactly did we get from "synthesizing MIDI" to here?
	return 0;
}
int g_test_subprocess() {
	return 0;
}

// gmain
void g_trace_mark(gint64 u0, gint64 u1, const gchar * u2, const gchar * u3, const gchar * u4, ...) {
}

// gfileutils
gchar * g_filename_display_name(const gchar * a) {
	return g_strdup(a);
}

// gstrfuncs
// notably, these two are used, once, as a pair - returning 1 here avoids the g_locale_to_utf8 call
gboolean g_get_console_charset(const char ** str) {
	return 1;
}
gchar * g_locale_to_utf8(const gchar * str, gssize u0, gsize * u4, gsize * u5, GError ** u6) {
	return g_strdup(str);
}

// printf
const gchar * g_dngettext(const gchar * u0, const gchar * text, const gchar * text2, gulong n) {
	return n == 1 ? text : text2;
}

void g_assertion_message(const char * u0, const char * u1, int u2, const char * u3, const char * u4) { abort(); }
void g_assertion_message_expr(const char * u0, const char * u1, int u2, const char * u3, const char * u4) { abort(); }
void g_assertion_message_cmpnum(const char * u0, const char * u1, int u2, const char * u3, const char * u4, long double u5, const char * u6, long double u7, char u8) { abort(); }

// printf stubs
void _g_gnulib_fprintf() {}
int _g_gnulib_snprintf(char *st, size_t sz, const char *fmt, ...) {
	if (sz)
		*st = 0;
	return 0;
}
int _g_gnulib_vsnprintf(char *st, size_t sz, const char *fmt) {
	return _g_gnulib_snprintf(st, sz, fmt);
}
void _g_gnulib_vprintf() {}
void _g_gnulib_vfprintf() {}
// printf stubs 2
int g_snprintf(char *st, gulong sz, const char *fmt, ...) {
	return _g_gnulib_snprintf(st, sz, fmt);
}
void g_vasprintf(char ** str, const char *fmt) {
	*str = g_strdup(fmt);
}
void g_vfprintf(void * o, const char *fmt) {}
void g_fprintf(void * o, const char *fmt) {}

