import { Component, Inject } from '@angular/core';
import {
  MAT_DIALOG_DATA,
  MatDialogActions,
  MatDialogClose,
  MatDialogContent,
  MatDialogTitle
} from '@angular/material/dialog';
import {MatIcon} from '@angular/material/icon';
import {MatButton, MatIconButton} from '@angular/material/button';
import {NgIf} from '@angular/common';

@Component({
  selector: 'app-share-dialog',
  template: `
    <h2 mat-dialog-title>Copied to clipboard! Choose a Platform to Share:</h2>
    <mat-dialog-content class="dialog-content">
      <div class="icon-container">
        <a *ngIf="data.availablePlatforms.email; else disabledIcon"
           [href]="data.availablePlatforms.email"
           target="_blank">
          <button mat-icon-button>
            <mat-icon>email</mat-icon>
          </button>
        </a>
        <ng-template #disabledIcon>
          <button mat-icon-button disabled>
            <mat-icon class="disabled">email</mat-icon>
          </button>
        </ng-template>

        <a *ngIf="data.availablePlatforms.facebook; else disabledFacebook"
           [href]="data.availablePlatforms.facebook"
           target="_blank">
          <button mat-icon-button>
            <mat-icon>facebook</mat-icon>
          </button>
        </a>
        <ng-template #disabledFacebook>
          <button mat-icon-button disabled>
            <mat-icon class="disabled">facebook</mat-icon>
          </button>
        </ng-template>

        <a *ngIf="data.availablePlatforms.whatsapp; else disabledWhatsapp"
           [href]="data.availablePlatforms.whatsapp"
           target="_blank">
          <button mat-icon-button>
            <mat-icon>chat</mat-icon>
          </button>
        </a>
        <ng-template #disabledWhatsapp>
          <button mat-icon-button disabled>
            <mat-icon class="disabled">chat</mat-icon>
          </button>
        </ng-template>

        <a *ngIf="data.availablePlatforms.instagram; else disabledInstagram"
           [href]="data.availablePlatforms.instagram"
           target="_blank">
          <button mat-icon-button>
            <mat-icon>camera_alt</mat-icon>
          </button>
        </a>
        <ng-template #disabledInstagram>
          <button mat-icon-button disabled>
            <mat-icon class="disabled">camera_alt</mat-icon>
          </button>
        </ng-template>

        <a *ngIf="data.availablePlatforms.telegram; else disabledTelegram"
           [href]="data.availablePlatforms.telegram"
           target="_blank">
          <button mat-icon-button>
            <mat-icon>send</mat-icon>
          </button>
        </a>
        <ng-template #disabledTelegram>
          <button mat-icon-button disabled>
            <mat-icon class="disabled">send</mat-icon>
          </button>
        </ng-template>
      </div>
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Close</button>
    </mat-dialog-actions>
  `,
  imports: [
    MatDialogActions,
    MatIcon,
    MatIconButton,
    MatButton,
    MatDialogClose,
    NgIf,
    MatDialogContent,
    MatDialogTitle
  ],
  styleUrls: ['./share-dialog.component.css']
})
export class ShareDialogComponent {
  constructor(@Inject(MAT_DIALOG_DATA) public data: { availablePlatforms: any }) {}
}
