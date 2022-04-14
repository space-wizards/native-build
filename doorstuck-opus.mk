# DOORSTUCK
include opus/opus_sources.mk
include opus/opus_headers.mk
include opus/silk_sources.mk
include opus/silk_headers.mk
include opus/celt_sources.mk
include opus/celt_headers.mk

OPUS_PFX := opus/

ALL_SOURCES := $(OPUS_SOURCES) $(OPUS_SOURCES_FLOAT)
ALL_SOURCES += $(CELT_SOURCES) $(CELT_SOURCES_SSE) $(CELT_SOURCES_SSE2)
ALL_SOURCES += $(SILK_SOURCES) $(SILK_SOURCES_FLOAT)

ALL_HEADERS := $(OPUS_HEAD) $(SILK_HEAD) $(CELT_HEAD)

ALL_SOURCES_PFX := $(addprefix $(OPUS_PFX),$(ALL_SOURCES))
ALL_HEADERS_PFX := $(addprefix $(OPUS_PFX),$(ALL_HEADERS))

# Includes
OPUS_CFLAGS := -I $(OPUS_PFX) -I $(OPUS_PFX)include -I $(OPUS_PFX)celt -I $(OPUS_PFX)silk -I $(OPUS_PFX)silk/float
# Defines
OPUS_CFLAGS += -DUSE_ALLOCA -DOPUS_BUILD
OPUS_CFLAGS += -DOPUS_X86_MAY_HAVE_SSE -DOPUS_X86_MAY_HAVE_SSE2
OPUS_CFLAGS += -DOPUS_X86_PRESUME_SSE -DOPUS_X86_PRESUME_SSE2
# Default to hidden visibility (Opus expects this and will override it's visibility for exports)
OPUS_CFLAGS += -fvisibility=hidden

# note the delayed evaluation
OPUS_LDFLAGS = -shared -o $@

all: builds/libopus.so builds/libopus.dll builds/libopus.dylib

builds/libopus.so: $(ALL_SOURCES_PFX) $(ALL_HEADERS_PFX)
	zig cc -target x86_64-linux-gnu $(OPUS_CFLAGS) $(ALL_SOURCES_PFX) $(OPUS_LDFLAGS)

builds/libopus.dll: $(ALL_SOURCES_PFX) $(ALL_HEADERS_PFX)
	zig cc -target x86_64-windows-gnu $(OPUS_CFLAGS) $(ALL_SOURCES_PFX) $(OPUS_LDFLAGS)

builds/libopus.dylib: $(ALL_SOURCES_PFX) $(ALL_HEADERS_PFX)
	zig cc -target x86_64-macos-gnu $(OPUS_CFLAGS) $(ALL_SOURCES_PFX) $(OPUS_LDFLAGS)

