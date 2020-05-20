<template>
    <v-card class="mt-4">
        <v-sheet class="v-sheet--offset d-flex mx-auto"
                 elevation="6"
                 max-width="calc(100% - 32px)"
                 :style="{'background-color': toggleColor}"
                 >
            <v-icon class="pa-6" large dark>mdi-camera</v-icon>
            <span class="font-weight-light d-flex align-center mr-auto white--text">Live Camera Feed</span>
            <v-card-actions class="pr-4">
                <v-btn @click="toggleCamera">
                    {{ cameraBtnTxt }}
                </v-btn>
            </v-card-actions>
        </v-sheet>
        <div id="camera">
            <video id="video">Video stream not available.</video>
        </div>
    </v-card>
</template>

<script>
    var video;

    export default {
        name: 'HomeCamera',
        data: function() {
            return { videoOn: true }
        },
        computed: {
            cameraBtnTxt() {
                return this.videoOn ? 'Off' : 'On'
            },
            toggleColor() {
                return this.videoOn ? '#14bd14' : 'red'
            }
        },
        mounted() {
            video = document.getElementById('video');
            this.toggleCamera();
        },
        methods: {
            toggleCamera() {
                if (video.srcObject == null) {
                    navigator.mediaDevices.getUserMedia({ video: true, audio: false })
                        .then(function (stream) {
                            video.srcObject = stream;
                            video.play();
                        })
                    this.videoOn = true;
                }
                else {
                    var stream = video.srcObject;
                    var tracks = stream.getTracks();

                    for (var i = 0; i < tracks.length; i++) {
                        var track = tracks[i];
                        track.stop();
                    }

                    video.srcObject = null;
                    this.videoOn = false;
                }
            }
        }
    };
</script>

<style scoped>
    #camera, #video {
        height: 400px;
    }

    #video {
        width: 100%;
        background-color: #000;
        -webkit-transform: scaleX(-1);
        transform: scaleX(-1);
    }
</style>