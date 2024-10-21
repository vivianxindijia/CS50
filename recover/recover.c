#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

#define BLOCK_SIZE 512
#define FILENAME_LENGTH 8

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s image\n", argv[0]);
        return 1;
    }

    //open the memory card
    FILE *forensicImage = fopen(argv[1], "r");
    if (forensicImage == NULL)
    {
        printf("Error: Could not open %s for reading.\n", argv[1]);
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];
    int jpegCount = 0;
    FILE *outputFILE = NULL;

    while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, forensicImage) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff & buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (outputFILE != NULL)
            {
                fclose(outputFILE);
            }

            char filename[FILENAME_LENGTH];
            sprintf(filename, "%03d.jpg", jpegCount);
            outputFILE = fopen(filename, "w");
            jpegCount++;
        }

        if (outputFILE != NULL)
        {
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, outputFILE);
        }
    }

    if (outputFILE != NULL)
    {
        fclose(outputFILE);
    }

    fclose(forensicImage);

    return 0;
}