#!/bin/bash

# This script is used internally in the Docker container.
# Don't run it directly. Run build-crosscompile-linux-macos.ps1 instead

cd /opt

# Build FluidSynth, the FUN way.
# This is very much an awful lot of "fake it till you make it" in build system form.
pushd fluidsynth
cd build
zig cc \
--target=x86_64-macos-gnu \
-D GLIB_COMPILATION \
-I ../../fluidsynth-macos-helpers \
-I . \
-I include \
-I ../include \
-I ../src \
-I ../src/bindings \
-I ../src/drivers \
-I ../src/gentables \
-I ../src/midi \
-I ../src/rvoice \
-I ../src/sfloader \
-I ../src/synth \
-I ../src/utils \
-I ../../glib \
-I ../../glib/glib \
../../glib/glib/gatomic.c \
../../glib/glib/garcbox.c \
../../glib/glib/grcbox.c \
../../glib/glib/gslist.c \
../../glib/glib/gslice.c \
../../glib/glib/ghash.c \
../../glib/glib/gstrfuncs.c \
../../glib/glib/gbytes.c \
../../glib/glib/gerror.c \
../../glib/glib/gmain.c \
../../glib/glib/glist.c \
../../glib/glib/gqueue.c \
../../glib/glib/gwakeup.c \
../../glib/glib/genviron.c \
../../glib/glib/gquark.c \
../../glib/glib/grefcount.c \
../../glib/glib/garray.c \
../../glib/glib/gstring.c \
../../glib/glib/gmem.c \
../../glib/glib/gtimer.c \
../../glib/glib/gvariant.c \
../../glib/glib/gbitlock.c \
../../glib/glib/glib-unix.c \
../../glib/glib/gvariant-core.c \
../../glib/glib/gvariant-parser.c \
../../glib/glib/gvariant-serialiser.c \
../../glib/glib/gvarianttype.c \
../../glib/glib/gvarianttypeinfo.c \
../../glib/glib/gqsort.c \
../../glib/glib/gmessages.c \
../../glib/glib/gthread.c \
../../glib/glib/gutf8.c \
../../glib/glib/gtranslit.c \
../../glib/glib/guri.c \
../../glib/glib/gutils.c \
../../glib/glib/glib-init.c \
../../glib/glib/gthread-posix.c \
../../glib/glib/gpoll.c \
../../glib/glib/ghostutils.c \
../../glib/glib/gunidecomp.c \
../../glib/glib/gshell.c \
../../glib/glib/guniprop.c \
../../glib/glib/gfileutils.c \
../../glib/glib/gstdio.c \
../../fluidsynth-macos-helpers/stubs.c \
../src/bindings/fluid_cmd.c \
../src/bindings/fluid_filerenderer.c \
../src/drivers/fluid_adriver.c \
../src/drivers/fluid_mdriver.c \
../src/midi/fluid_midi.c \
../src/midi/fluid_midi_router.c \
../src/midi/fluid_seq.c \
../src/midi/fluid_seqbind.c \
../src/rvoice/fluid_adsr_env.c \
../src/rvoice/fluid_chorus.c \
../src/rvoice/fluid_iir_filter.c \
../src/rvoice/fluid_lfo.c \
../src/rvoice/fluid_rev.c \
../src/rvoice/fluid_rvoice.c \
../src/rvoice/fluid_rvoice_dsp.c \
../src/rvoice/fluid_rvoice_event.c \
../src/rvoice/fluid_rvoice_mixer.c \
../src/sfloader/fluid_defsfont.c \
../src/sfloader/fluid_samplecache.c \
../src/sfloader/fluid_sffile.c \
../src/sfloader/fluid_sfont.c \
../src/synth/fluid_chan.c \
../src/synth/fluid_event.c \
../src/synth/fluid_gen.c \
../src/synth/fluid_mod.c \
../src/synth/fluid_synth.c \
../src/synth/fluid_synth_monopoly.c \
../src/synth/fluid_tuning.c \
../src/synth/fluid_voice.c \
../src/utils/fluid_conv.c \
../src/utils/fluid_hash.c \
../src/utils/fluid_list.c \
../src/utils/fluid_ringbuffer.c \
../src/utils/fluid_settings.c \
../src/utils/fluid_sys.c \
-shared \
-fPIC \
-o libfluidsynth.dylib
popd

